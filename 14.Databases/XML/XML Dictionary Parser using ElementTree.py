#!/usr/bin/env python
"""
XML Dictionary Parser using ElementTree

This module demonstrates how to parse XML files and convert them into Python dictionaries
with proper type casting based on XML attributes.
"""

import xml.etree.ElementTree as ET

# Type mapping for converting string values to their respective Python types
TYPE_MAPPING = {
    "int": int,
    "str": str,
    "float": float,
    "bool": lambda x: x.lower() in ("true", "1", "yes")
}


def read_element(element):
    """
    Read an XML element and convert its text content to the appropriate Python type.
    
    Args:
        element: An XML Element object with optional 'typ' attribute
        
    Returns:
        The element's text content converted to the specified type (defaults to str)
    """
    element_type = element.get("typ", "str")
    
    # Return None if element has no text content
    if element.text is None:
        return None
    
    # Convert to the specified type, fallback to string if type is unknown
    converter = TYPE_MAPPING.get(element_type, str)
    try:
        return converter(element.text)
    except (ValueError, AttributeError) as e:
        print(f"Warning: Could not convert '{element.text}' to type '{element_type}': {e}")
        return element.text


def load_dict_from_xml(filename):
    """
    Load a dictionary from an XML file with the following structure:
    <dictionary>
        <eintrag>
            <schluessel typ="str">key</schluessel>
            <wert typ="int">value</wert>
        </eintrag>
    </dictionary>
    
    Args:
        filename: Path to the XML file to parse
        
    Returns:
        dict: A dictionary with keys and values extracted from the XML
        
    Raises:
        FileNotFoundError: If the XML file doesn't exist
        ET.ParseError: If the XML file is malformed
    """
    # Parse the XML file
    tree = ET.parse(filename)
    root = tree.getroot()
    
    # Build dictionary from XML entries
    result = {}
    for entry in root:
        key_element = entry.find("schluessel")
        value_element = entry.find("wert")
        
        # Skip entries with missing key or value elements
        if key_element is None or value_element is None:
            print(f"Warning: Skipping entry with missing key or value element")
            continue
        
        key = read_element(key_element)
        value = read_element(value_element)
        result[key] = value
    
    return result


if __name__ == "__main__":
    try:
        dictionary = load_dict_from_xml("dict.xml")
        print("Loaded dictionary from XML:")
        print(dictionary)
    except FileNotFoundError:
        print("Error: dict.xml file not found")
    except ET.ParseError as e:
        print(f"Error: Failed to parse XML file: {e}")
