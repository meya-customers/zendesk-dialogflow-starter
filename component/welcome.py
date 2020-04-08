from dataclasses import dataclass
from meya.element.engine.component import ComponentElement
from meya.element.field import element_field
from meya.entry import Entry
from meya.entry.event import MeyaSayEvent
from typing import List


@dataclass
class WelcomeComponentElement(ComponentElement):
    language: str = element_field()

    async def start(self) -> List[Entry]:
        if self.language == "en":
            text = "Welcome! Let's get started!"
        elif self.language == "fr":
            text = "Bienvenue! Commençons!"
        else:
            text = "🤔"
        text_event = MeyaSayEvent(
            composer=None,
            member_id=self.member_id,
            quick_replies=None,
            text=text,
            thread_id=self.entry.thread_id,
        )
        return self.respond(text_event)
