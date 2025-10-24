from fastapi import HTTPException
import re

def validate_product_input(data: dict) -> None:
    """
    Valida la entrada de datos de productos contra inyecciones y datos maliciosos
    Protección contra:
    - A03:2021 - Injection
    - A04:2021 - Insecure Design
    
    Args:
        data (dict): Datos del producto a validar
        
    Raises:
        HTTPException: Si los datos contienen contenido potencialmente malicioso
    """
    # Patrones de validación
    patterns = {
        'script_pattern': r'<script|javascript:|data:',
        'sql_pattern': r'(\b(ALTER|CREATE|DELETE|DROP|EXEC(UTE){0,1}|INSERT( +INTO){0,1}|MERGE|SELECT|UPDATE|UNION( +ALL){0,1})\b)',
        'special_chars': r'[<>]'
    }
    
    for field, value in data.items():
        if not isinstance(value, (str, int, float, bool)):
            continue
            
        value_str = str(value)
        
        # Verificar inyección de scripts
        if re.search(patterns['script_pattern'], value_str, re.I):
            raise HTTPException(
                status_code=400,
                detail=f"Contenido no permitido en el campo {field}"
            )
            
        # Verificar inyección SQL
        if re.search(patterns['sql_pattern'], value_str, re.I):
            raise HTTPException(
                status_code=400,
                detail=f"Contenido no permitido en el campo {field}"
            )
            
        # Verificar caracteres especiales
        if re.search(patterns['special_chars'], value_str):
            raise HTTPException(
                status_code=400,
                detail=f"Caracteres no permitidos en el campo {field}"
            )

def sanitize_output(data: dict) -> dict:
    """
    Sanitiza los datos de salida para prevenir XSS y fugas de información
    Protección contra:
    - A03:2021 - Injection
    - A04:2021 - Insecure Design
    
    Args:
        data (dict): Datos a sanitizar
        
    Returns:
        dict: Datos sanitizados
    """
    if isinstance(data, dict):
        return {k: sanitize_output(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [sanitize_output(i) for i in data]
    elif isinstance(data, str):
        # Escapar caracteres especiales
        return (data.replace('&', '&amp;')
                   .replace('<', '&lt;')
                   .replace('>', '&gt;')
                   .replace('"', '&quot;')
                   .replace("'", '&#x27;'))
    return data