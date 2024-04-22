from textnode import TextNode, text_type_bold, text_type_code, text_type_image, text_type_italic, text_type_link, text_type_text
import re


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    # take in a list of TextNodes but only process the ones with text_type as text_type_text
    all_nodes_created = []
    for node in old_nodes:
        if node.text_type != text_type_text:
            all_nodes_created.append(node)
            continue

        sessions = node.text.split(delimiter)
        if len(sessions) % 2 == 0:
            raise Exception("Section not closed with delimiter.")
        
        nodes_created = []
        for i in range(len(sessions)):
            if sessions[i] == "":
                continue
            if i % 2 == 0: # will always be odd-numbered. only the middle ones are of interest
                nodes_created.append(TextNode(sessions[i], text_type_text))
            else:
                nodes_created.append(TextNode(sessions[i], text_type))
        all_nodes_created.extend(nodes_created)

    return all_nodes_created


def extract_markdown_images(text):
    # takes raw text and returns a list of tuples. 
    # each tuple should contain all alt text and the URL of any markdown images.
    image_pattern = r"!\[(.*?)\]\((.*?)\)"
    matches = re.findall(image_pattern, text)
    return matches


def extract_markdown_links(text):
    # extract markdown links instead of images.
    # it should return tuples of anchor text and URLs.
    link_pattern = r"\[(.*?)\]\((.*?)\)"
    matches = re.findall(link_pattern, text)
    return matches



def split_nodes_image(old_nodes):
    all_created_nodes = []
    for node in old_nodes:
        extracted_tups = extract_markdown_images(node.text)
        # If there are no images, put the textnode back as is
        if len(extracted_tups) == 0:
            all_created_nodes.append(node)
            continue
        text = node.text
        for tup in  extracted_tups:
            sessions = text.split("![{}]({})".format(tup[0], tup[1]), 1) # split at most 1 time
            all_created_nodes.append(TextNode(sessions[0], text_type_text))
            all_created_nodes.append(TextNode(tup[0], text_type_image, tup[1]))
            text = sessions[1]
        # If the last split has something on the right side of split.
        if text:
            all_created_nodes.append(TextNode(text, text_type_text))
    return all_created_nodes



def split_nodes_link(old_nodes):
    all_created_nodes = []
    for node in old_nodes:
        extracted_tups = extract_markdown_links(node.text)
        # If there are no images, put the textnode back as is
        if len(extracted_tups) == 0:
            all_created_nodes.append(node)
            continue
        text = node.text
        for tup in  extracted_tups:
            sessions = text.split("[{}]({})".format(tup[0], tup[1]), 1)
            all_created_nodes.append(TextNode(sessions[0], text_type_text))
            all_created_nodes.append(TextNode(tup[0], text_type_link, tup[1]))
            text = sessions[1]
        # If the last split has something on the right side of split.
        if text:
            all_created_nodes.append(TextNode(text, text_type_text))
    return all_created_nodes


def text_to_textnodes(text):
    # Put all the "splitting" functions together into a function that can convert a raw string of 
    # markdown flavored text into a list of TextNode objects.
    node = TextNode(text, text_type_text)
    nodes = split_nodes_delimiter([node], "**", text_type_bold)
    nodes = split_nodes_delimiter(nodes, "*", text_type_italic)
    nodes = split_nodes_delimiter(nodes, "`", text_type_code)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes










