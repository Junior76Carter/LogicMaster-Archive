def execute_binary_analysis(bit_stream):
    """
    Performs a comprehensive logic analysis by decoding raw binary 
    input into decimal and hexadecimal representations.
    
    Args:
        bit_stream (str): A string consisting of binary digits (0 and 1).
        
    Returns:
        dict: A collection containing the processed data formats.
    """
    try:
        # Validate and convert binary string to integer base
        decimal_representation = int(bit_stream, 2)
        
        # Format the decimal value into a standard Hexadecimal string
        hexadecimal_output = hex(decimal_representation).upper()
        
        analysis_report = {
            "Input": bit_stream,
            "Decimal": decimal_representation,
            "Hexadecimal": hexadecimal_output
        }
        
        print("--- [ SYSTEM LOGIC REPORT ] ---")
        print(f"Status: Data integrity verified.")
        print(f"Mapped Decimal: {analysis_report['Decimal']}")
        print(f"Mapped Hex: {analysis_report['Hexadecimal']}")
        print("--- [ ANALYSIS COMPLETE ] ---")
        
        return analysis_report

    except ValueError:
        print("Critical Error: Invalid bit stream detected. Operation aborted.")

# Demonstration of the logic mapping capability
if __name__ == "__main__":
    execute_binary_analysis("101101")
