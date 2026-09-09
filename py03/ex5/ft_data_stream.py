#!/usr/bin/python3

from typing import Generator
import random

Event = tuple[str, str]

def gen_event() -> Generator[Event, None, None]:
    names: list[str] = [
        "alice",
        "bob",
        "charlie",
        "diana",
        "felix",
        "gilbert",
    ]

    actions: list[str] = [
        "joined the game",
        "found a treasure",
        "defeated an enemy",
        "left the game",
        "began chinofarming"
    ]

    while True:
        name: str = random.choice(names)
        action: str = random.choice(actions)

        yield name, action


def fill_list(gen: Generator[Event, None, None], nbr: int) -> list[Event]:
    events: list[Event] = []
    if nbr < 0:
        raise ValueError("Can't fill the list with a negative quantity")

    for _ in range(nbr):
        events.append(next(gen))
    return events


def consume_event(events: list[Event]) -> Generator[Event, None, None]:
    while len(events) > 0:
        index: int = random.randrange(len(events))
        event: Event = events.pop(index)
        yield event


def ft_data_stream() -> None:
    event_generator: Generator[Event, None, None] = gen_event()
    for i in range(1, 1001):
        new_event: Event = next(event_generator)
        message: str = f"Day {i}: "
        message += (f"{new_event[0]} {new_event[1]}")
        print(message)
    try:
        events_list: list[Event] = fill_list(event_generator, 10)
        print(f"Built list of {len(events_list)}: {events_list}")
        for event in consume_event(events_list):
            print(f"Got event from list{event}")
            print(f"=== Remains in list: {events_list}")
    except ValueError as e:
        print(f"What??: {e}")

if __name__ == "__main__":
    print(f"=== Inventory System Analysis ===")
    print()
    ft_data_stream()
    print()
    print("=== End Of Program ===")
