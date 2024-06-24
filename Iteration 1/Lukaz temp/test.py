class Some:
    def __init__(self, content):
        self.content = content

hair_colour = Some("white")

section_dict ={
    "Gender": 0,
    "Hair": [hair_colour]
}

menu_option= "Hair"
print(hair_colour.content)

section_dict[menu_option][0].content = ("black")

print(hair_colour.content)