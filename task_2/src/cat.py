from dataclasses import dataclass


@dataclass
class Cat:
    nickname: str
    age: int
    breed: str
    img_path: str
    description: str
