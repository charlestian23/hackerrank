let rec reverse_list = function
  | [] -> []
  | h :: t -> reverse_list t @ [ h ]

let rec get_input array =
  try
    let input = read_line() in
    match input with 
      | "" -> array
      | x -> get_input(array @ [x])
  with End_of_file -> array

let rec print_list = function
  | [] -> print_string ""
  | h::t -> print_endline h ; print_list t

let _ = print_list(reverse_list(get_input []))