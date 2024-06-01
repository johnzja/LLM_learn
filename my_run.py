from datetime import datetime
import os
import argparse
import matplotlib.pyplot as plt
from rich.console import Console
import numpy as np
from copy import deepcopy

import instructor
from openai import OpenAI
import tenacity
from pydantic import BaseModel


class PersonalInfo(BaseModel): 
    name: str
    age: int 
    profession: str



if __name__ == '__main__':

    description_1 = "Please tell me who is Jieao Zhu in China.\n" 

    client = instructor.from_openai(OpenAI())
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        temperature=0,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."}, 
            {"role": "user", "content": description_1}, 
        ],
        response_model=PersonalInfo, 
        max_tokens=1000,
        max_retries=tenacity.Retrying(
            stop=tenacity.stop_after_attempt(4),
        ),
    )

    
    print(completion.name)
    print(completion.age)
    print(completion.profession)
    pass





    



