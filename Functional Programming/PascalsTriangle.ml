let rec factorial = function
  | 0 | 1 -> 1
  | n -> n * factorial (n - 1)

let calculate n r = (factorial n) / ((factorial r) * (factorial (n - r)))

let rec print_pascal_row row = function
  | col when col = row -> print_endline("1")
  | col -> print_string ((string_of_int (calculate row col)) ^ " ") ; print_pascal_row row (col + 1)

let rec print_pascal rows n =
  let _ = print_pascal_row n 0 in
  if n != rows then print_pascal rows (n + 1)

let rows = int_of_string (read_line ())
let _ = print_pascal (rows - 1) 0