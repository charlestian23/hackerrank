let rec print_under_n n = function
  | [] -> print_string("")
  | h::t -> if h < n then print_endline(string_of_int(h)) ; print_under_n n t

let rec get_input array =
  try
    let input = read_line() in
    match input with 
      | "" -> array
      | x -> get_input(array @ [int_of_string x])
  with End_of_file -> array

let n = read_int()
let array = get_input []
let _ = print_under_n n array