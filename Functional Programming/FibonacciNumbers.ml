let rec fibonacci = function
  | 1 -> 0
  | 2 -> 1
  | n -> fibonacci (n - 1) + fibonacci (n - 2)

let n = read_int()
let _ = print_int (fibonacci n)