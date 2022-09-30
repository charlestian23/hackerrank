let rec length len =
  try
    let input = read_line() in
    match input with 
      | "" -> len
      | x -> length len + 1
  with End_of_file -> len

let _ = print_int (length 0)