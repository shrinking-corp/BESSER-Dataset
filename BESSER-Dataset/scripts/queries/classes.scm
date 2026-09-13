; Every class definition, anywhere in the file (top-level or nested).
; Decorators (e.g. @dataclass) are NOT captured here -- a decorated class is
; wrapped in a `decorated_definition` node one level up, so the Python side
; checks `class_node.parent` for that wrapper instead of matching it here.
(class_definition
  name: (identifier) @class.name
  superclasses: (argument_list)? @class.superclasses
  body: (block) @class.body) @class.def
