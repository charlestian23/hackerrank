let rec read_lines () =
  try let line = read_line () in
      int_of_string (line) :: read_lines()
  with
      End_of_file -> []

(* Complete this function *)
let rec f n arr =
  let rec make n item =
    match n with
    | 0 -> []
    | x -> item :: (make (n - 1) item) in
  match arr with
  | [] -> []
  | h::t -> (make n h) @ (f n t)

let () =
  let n::arr = read_lines() in
  let ans = f n arr in
  List.iter (fun x -> print_int x; print_newline ()) ans;;