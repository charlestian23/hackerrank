let rec print_n_times = function
  | 0 -> print_string("")
  | n -> print_endline("Hello World") ; print_n_times (n - 1)

let n = read_int()
let _ = print_n_times n