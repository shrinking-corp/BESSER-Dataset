; Class variable: `name = value` or `name: Type = value` assigned directly in
; a class body (not inside a method). @attribute.owner captures the
; enclosing class_definition directly, so no parent-walking is needed for
; this pattern (unlike the self.x one below).
(class_definition
  body: (block
    (expression_statement
      (assignment
        left: (identifier) @attribute.name
        type: (type)? @attribute.type
        right: (_)? @attribute.value) @attribute.assignment))) @attribute.owner

; Instance attribute: `self.name = value` or `self.name: Type = value`,
; anywhere in the file. Restricted to `self` (not `cls` or other receiver
; names) by the predicate below. The Python side keeps only the ones found
; inside a class's `__init__` -- see extract_structure.py for why.
(assignment
  left: (attribute
    object: (identifier) @attribute.self
    attribute: (identifier) @attribute.name)
  type: (type)? @attribute.type
  right: (_)? @attribute.value
  (#eq? @attribute.self "self")) @attribute.assignment
