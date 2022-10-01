let rec e_to_x x power factorial =
  if power > 9.0 then 1.0
  else
    let new_power = power +. 1.0 in
    let new_factorial = factorial *. new_power in
    (x ** power) /. factorial +. (e_to_x x new_power new_factorial)

let rec parse_input = function
  | 0 -> print_string("")
  | n -> let x = read_float() in print_endline(string_of_float(e_to_x x 1.0 1.0)) ; parse_input (n - 1)
    
let inputs = read_int()
let _ = parse_input inputs
