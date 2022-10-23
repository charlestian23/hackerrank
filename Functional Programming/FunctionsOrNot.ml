module IntMap = Map.Make(struct type t = int let compare = compare end)

let read_int_value () = read_line () |> String.trim |> int_of_string

let rec read_garbage = function
  | 0 -> "NO"
  | n -> let _ = read_line () in read_garbage (n - 1)

let rec is_function map = function
  | 0 -> "YES"
  | n -> let temp = String.split_on_char ' ' (String.trim (read_line ())) in
    let key = int_of_string (String.trim (List.nth temp 0)) in
    let value = int_of_string (String.trim (List.nth temp 1)) in
    if IntMap.find_opt key map = None then let map = IntMap.add key value map in is_function map (n - 1)
    else if IntMap.find key map != value then read_garbage (n - 1)
    else is_function map (n - 1)

let rec parse_input = function
  | 0 -> print_string ""
  | n -> let map = IntMap.empty in
    let _ = print_endline (is_function map (read_int_value())) in
    parse_input (n - 1)

let inputs = read_int_value()
let _ = parse_input inputs;
