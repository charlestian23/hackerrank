(* returns an array of n elements *)
let rec make_array n =
  if n = 0 then []
  else 0 :: make_array (n - 1)

let () =
    let n = int_of_string (read_line ()) in
    let arr = make_array n in
    List.iter ( Printf.printf "%d " ) arr