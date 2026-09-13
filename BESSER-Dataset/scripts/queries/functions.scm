; Every function definition, anywhere in the file. This matches both
; top-level functions and methods -- the Python side tells them apart by
; walking up to the nearest enclosing class_definition (if any).
(function_definition
  name: (identifier) @function.name
  parameters: (parameters) @function.parameters
  return_type: (type)? @function.return_type
  body: (block) @function.body) @function.def
