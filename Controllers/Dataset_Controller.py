from __future__ import annotations

from typing import Any, Dict, List

from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QDialog

# change this import to wherever your view class lives
# from Views.DatasetConfigDialog import DatasetConfigDialog


class Dataset_Controller(QDialog):



    def __init__(self, model,view,parent=None):
        super().__init__(parent)
        self.model = model
        self.view = view



        self.view.setupUi(self)

        self._connect_signals()
        self._apply_initial_state()
        self.configure_options_by_task()




    def configure_options_by_task(self):
        task = self.model.get_task_type().lower()

        if task == "classification":
            self.view.task_entry.setCurrentText("Classification")
            self.view.task_entry.setEnabled(False)  # Lock the task selection since it's determined by the model
            self.view.label_mode_entry.setVisible(True)  # Hide label mode since regression doesn't use it
            self.view.label_mode_label.setVisible(True)

        if task == "regression":
            self.view.task_entry.setCurrentText("Regression")
            self.view.task_entry.setEnabled(False)  # Lock the task selection since it's determined by the model
            self.view.label_mode_entry.setVisible(False)  # Hide label mode since regression doesn't use it
            self.view.label_mode_label.setVisible(False)

    # -----------------------------
    # Setup helpers
    # -----------------------------
    def _connect_signals(self) -> None:
        self.view.task_entry.currentIndexChanged.connect(self._update_visibility)
        self.view.label_mode_entry.currentIndexChanged.connect(self._update_visibility)
        self.view.feature_mode_entry.currentIndexChanged.connect(self._update_visibility)


        self.view.main_button.clicked.connect(self.handle_next_button)

    def _apply_initial_state(self) -> None:
        self._update_visibility()

    # -----------------------------
    # UI state logic
    # -----------------------------
    def _update_visibility(self) -> None:

        # TODO: some of this code isnt nessary as widgets are hidden based on the task type given by the model metadata
        """
        Show/hide widgets based on the current dataset config selections.
        This keeps the UI cleaner than disabling irrelevant fields.
        """

        task = self.view.task_entry.currentText().strip().lower()
        label_mode = self.view.label_mode_entry.currentText().strip().lower()
        feature_mode = self.view.feature_mode_entry.currentText().strip().lower()

        is_classification = task == "classification"
        is_existing_label = label_mode == "existing label column"
        is_pct_bins = label_mode == "percent change bins"
        is_pct_numeric = label_mode == "percent change numeric"
        use_first_n = feature_mode == "use first n columns"
        use_manual_features = feature_mode == "select columns manually"

        # -----------------------------
        # Target / Label column widgets
        # -----------------------------
        self.view.target_col_label.setVisible(not is_existing_label)
        self.view.target_col_entry.setVisible(not is_existing_label)

        self.view.label_col_label.setVisible(is_existing_label)
        self.view.label_col_entry.setVisible(is_existing_label)

        # -----------------------------
        # Horizon widgets
        # existing label column usually doesn't need horizon
        # -----------------------------
        show_horizon = not is_existing_label
        self.view.horizon_label.setVisible(show_horizon)
        self.view.horizon_entry.setVisible(show_horizon)

        # -----------------------------
        # Classification options group
        # only show for classification + percent change bins
        # -----------------------------
        show_class_group = is_classification and is_pct_bins
        self.view.class_group.setVisible(show_class_group)

        # -----------------------------
        # Feature mode widgets
        # -----------------------------
        self.view.feature_count_label.setVisible(use_first_n)
        self.view.feature_count_entry.setVisible(use_first_n)

        # If you're using the preview field as manual-entry for now,
        # show it only for manual mode.
        self.view.feature_preview_label.setVisible(use_manual_features)
        self.view.feature_preview_entry.setVisible(use_manual_features)

        # If you later add a real selector button, use this:
        if hasattr(self.view, "feature_select_button"):
            self.view.feature_select_button.setVisible(use_manual_features)

        # -----------------------------
        # Optional: adjust group visibility if empty
        # -----------------------------
        # Usually keep features_group visible because one of its modes is always relevant.
        self.view.features_group.setVisible(True)

        # -----------------------------
        # Optional: force layout refresh
        # -----------------------------
        self.adjustSize()
    # -----------------------------
    # Button handlers
    # -----------------------------


    def handle_next_button(self):
        config = self.get_config_dict()
        error = self.validate_config(config)

        if error is not None:
            QtWidgets.QMessageBox.warning(self, "Invalid Dataset Config", error)
            return

        self.accept()

    # -----------------------------
    # Public API
    # -----------------------------
    def get_config_dict(self) -> Dict[str, Any]:
        """
        Returns a normalized dict of all dataset config entries.
        """

        feature_mode_text = self.view.feature_mode_entry.currentText().strip()
        feature_preview_text = self.view.feature_preview_entry.text().strip()

        config: Dict[str, Any] = {
            "task": self.view.task_entry.currentText().strip(),
            "label_mode": self.view.label_mode_entry.currentText().strip(),
            "target_col": self.view.target_col_entry.value(),
            "label_col": self.view.label_col_entry.value(),
            "horizon": self.view.horizon_entry.value(),
            "feature_mode": feature_mode_text,
            "feature_count": self.view.feature_count_entry.value(),
            "feature_preview": feature_preview_text,
            "feature_columns": self._parse_feature_columns(feature_preview_text),
            "stride": self.view.stride_entry.value(),
            "sampling_mode": self.view.sampling_entry.currentText().strip(),
            "max_windows_per_file": self.view.max_windows_entry.value(),
            "seed": self.view.seed_entry.value(),
            "skip_first_row": self.view.skip_first_row_entry.isChecked(),
            "num_classes": self.view.classes_entry.value(),
            "bin_min": self.view.bin_min_entry.value(),
            "bin_max": self.view.bin_max_entry.value(),
        }

        return config

    def validate_config(self, config: Dict[str, Any]) -> str | None:
        """
        Returns an error string if invalid, else None.
        """

        task = config["task"].lower()
        label_mode = config["label_mode"].lower()
        feature_mode = config["feature_mode"].lower()

        if task not in {"classification", "regression"}:
            return "Task must be Classification or Regression."

        if label_mode not in {
            "percent change bins",
            "percent change numeric",
            "existing label column",
        }:
            return "Unsupported label mode selected."

        if label_mode == "existing label column":
            if config["label_col"] < 0:
                return "Label column must be 0 or greater."
        else:
            if config["target_col"] < 0:
                return "Target column must be 0 or greater."

        if config["horizon"] < 1 and label_mode != "existing label column":
            return "Horizon must be at least 1."

        if feature_mode == "use first n columns":
            if config["feature_count"] < 1:
                return "Feature count must be at least 1."
        else:
            if not config["feature_columns"]:
                return "Please provide feature columns for manual selection."

        if config["stride"] < 1:
            return "Stride must be at least 1."

        if config["max_windows_per_file"] < 1:
            return "Max windows per file must be at least 1."

        if task == "classification" and label_mode == "percent change bins":
            if config["num_classes"] < 2:
                return "Number of classes must be at least 2."
            if config["bin_min"] >= config["bin_max"]:
                return "Bin Range Min must be less than Bin Range Max."

        return None

    # -----------------------------
    # Parsing helpers
    # -----------------------------
    def _parse_feature_columns(self, text: str) -> List[int]:
        """
        Parses comma-separated feature indices from the preview field.

        Example:
            "0, 1, 2, 3" -> [0, 1, 2, 3]
        """
        if not text:
            return []

        result: List[int] = []
        for part in text.split(","):
            cleaned = part.strip()
            if not cleaned:
                continue
            try:
                result.append(int(cleaned))
            except ValueError:
                # Ignore bad values for now; validation can handle missing/empty cases
                pass
        return result


