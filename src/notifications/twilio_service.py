import logging

logger = logging.getLogger(__name__)


class TwilioNotificationService:
    """Anulează complet apelurile externe Twilio și le redirectează în consolă."""

    def __init__(
        self,
        account_sid: str | None = None,
        auth_token: str | None = None,
        from_number: str | None = None,
    ):
        self.account_sid = account_sid
        self.auth_token = auth_token
        self.from_number = from_number
        logger.info(
            "[OFFLINE MODE] TwilioNotificationService inițializat în mod simulare locală."
        )

    def send_sms(self, to_number: str, message: str) -> bool:
        """Afișează SMS-ul de alertă direct în terminal, fără a folosi internetul."""
        print("\n" + "=" * 60)
        print("📟 [SIMULARE SMS LOCALĂ - GATEWAY TWILIO ANULAT]")
        print(f"Către: {to_number}")
        print(f"Mesaj: {message}")
        print("=" * 60 + "\n")
        return True
