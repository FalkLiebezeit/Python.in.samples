#!/usr/bin/env python
"""
XML Dictionary Parser using SAX

This module demonstrates how to parse XML files using SAX (Simple API for XML),
which is more memory-efficient than DOM parsing for large files as it processes
the XML sequentially without loading the entire document into memory.
"""

import os
import xml.sax as sax


class DictionaryHandler(sax.handler.ContentHandler):
    """
    SAX Content Handler for parsing XML dictionary entries.
    
    Handles XML with the structure:
    <dictionary>
        <eintrag>
            <schluessel typ="str">key</schluessel>
            <wert typ="int">value</wert>
        </eintrag>
    </dictionary>
    """
    
    # Type mapping for converting string values to Python types
    TYPE_MAPPING = {
        "int": int,
        "str": str,
        "float": float,
        "bool": lambda x: x.lower() in ("true", "1", "yes")
    }

    def __init__(self):
        """Initialize the handler with empty state."""
        super().__init__()
        self.result = {}  # Final dictionary result
        self.current_key = ""  # Current key being processed
        self.current_value = ""  # Current value being processed
        self.active_element = None  # Currently active element ('schluessel' or 'wert')
        self.value_type = str  # Type converter for current value

    def startElement(self, name, attrs):
        """
        Called when an opening XML tag is encountered.
        
        Args:
            name: Name of the XML element
            attrs: Attributes of the XML element
        """
        if name == "eintrag":
            # Start of a new dictionary entry - reset current key and value
            self.current_key = ""
            self.current_value = ""
            self.value_type = str
            
        elif name in ("schluessel", "wert"):
            # Start reading key or value element
            self.active_element = name
            
            # Determine type converter from 'typ' attribute
            type_name = attrs.get("typ", "str")
            self.value_type = self.TYPE_MAPPING.get(type_name, str)

    def endElement(self, name):
        """
        Called when a closing XML tag is encountered.
        
        Args:
            name: Name of the XML element being closed
        """
        if name == "eintrag":
            # End of dictionary entry - store key-value pair
            try:
                # Convert value to appropriate type and store in result
                converted_value = self.value_type(self.current_value.strip())
                self.result[self.current_key.strip()] = converted_value
            except (ValueError, TypeError) as e:
                print(f"Warning: Could not convert value '{self.current_value}' - using string instead: {e}")
                self.result[self.current_key.strip()] = self.current_value.strip()
                
        elif name in ("schluessel", "wert"):
            # End of key or value element - stop accumulating content
            self.active_element = None

    def characters(self, content):
        """
        Called when character data is encountered between XML tags.
        SAX may call this method multiple times for a single element's content.
        
        Args:
            content: Character data from the XML
        """
        if self.active_element == "schluessel":
            # Accumulate key content
            self.current_key += content
        elif self.active_element == "wert":
            # Accumulate value content
            self.current_value += content


def load_dict_from_xml(filename):
    """
    Load a dictionary from an XML file using SAX parsing.
    
    SAX parsing is more memory-efficient than DOM parsing (ElementTree)
    for large XML files because it processes the file sequentially
    without loading the entire document into memory.
    
    Args:
        filename: Path to the XML file to parse
        
    Returns:
        dict: A dictionary with keys and values extracted from the XML
        
    Raises:
        FileNotFoundError: If the XML file doesn't exist
        sax.SAXException: If the XML file is malformed
    """
    # Resolve the file path to absolute path
    if not os.path.isabs(filename):
        # If relative path, make it relative to this script's directory
        script_dir = os.path.dirname(os.path.abspath(__file__))
        filename = os.path.join(script_dir, filename)
    
    # Check if file exists
    if not os.path.exists(filename):
        raise FileNotFoundError(f"XML file not found: {filename}")
    
    # Create handler and parser
    handler = DictionaryHandler()
    parser = sax.make_parser()
    parser.setContentHandler(handler)
    
    # Parse the XML file
    parser.parse(filename)
    
    return handler.result


if __name__ == "__main__":
    try:
        dictionary = load_dict_from_xml("dict.xml")
        print("Loaded dictionary from XML using SAX:")
        print(dictionary)
    except FileNotFoundError:
        print("Error: dict.xml file not found")
    except sax.SAXException as e:
        print(f"Error: Failed to parse XML file: {e}")
