let rec gcd a b =
  if a = 0 then b
  else if b = 0 then a
  else gcd b (a mod b)

let rec split str = str |> String.split_on_char ' ' |> List.filter (fun s -> s <> "")

let input = split (read_line ())
let a = int_of_string (List.nth input 0)
let b = int_of_string (List.nth input 1)
let _ = print_int(gcd a b)