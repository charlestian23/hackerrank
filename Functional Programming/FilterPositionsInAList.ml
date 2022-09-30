let rec filter n =
  try
    let input = read_line() in
    match input with 
      | "" -> print_string("")
      | x -> if n mod 2 = 1 then print_endline(x) ; filter (n + 1)
  with End_of_file -> print_string("")

let _ = filter 0