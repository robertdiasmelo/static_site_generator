from textnode import  TextNode, TextType

def main():
    my_text_node = TextNode("My current lesson", TextType.BOLD_TEXT, "https://www.boot.dev/lessons/cdae7fca-a7dc-4706-b2c5-7a03d66db1c9")
    print(my_text_node)


if __name__ == "__main__":
    main()