"""Clinical Event Logging and Diagnostics System Configuration.

Establishes synchronized stream output log formatters to track real-time
biomarker shifts, prompt injections, and network transaction states.
"""

import logging
import sys


def configure_system_logging() -> logging.Logger:
    """Instantiates and binds standard enterprise formatters to the root clinical logger framework.

    Returns:
        logging.Logger: A configured synchronized system diagnostic logger instance.
    """
    logger = logging.getLogger("NICU_Sepsis_Monitor")

    if not logger.handlers:
        logger.setLevel(logging.INFO)

        # Build a robust industrial log line layout pattern
        log_format = logging.Formatter(
            "[%(asctime)s] [%(levelname)s] [%(filename)s:%(lineno)d]: %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )

        # Bind a safe console standard out handler target
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(log_format)
        logger.addHandler(console_handler)

    return logger
