let rec split str = str |> String.split_on_char ' ' |> List.filter (fun s -> s <> "")

let rec f func x =
  match func with
  | [] -> 0.0
  | (a, b) :: t -> (a *. (x ** b)) +. f t x

let rec area func a b subinterval =
  if a >= b then 0.0 else f func a *. subinterval +. area func (a +. subinterval) b subinterval

let rec volume func a b subinterval =
  if a >= b then 0.0
  else
    ((f func a ** 2.0) *. subinterval *. Float.pi) +. volume func (a +. subinterval) b subinterval

let rec get_function coeffs expons list =
  match (coeffs, expons) with
  | [], [] | _, [] | [], _ -> list
  | hc :: tc, he :: te -> get_function tc te ((float_of_string hc, float_of_string he) :: list)

let coefficients = split (read_line ())
let exponents = split (read_line ())
let func = get_function coefficients exponents []
let temp = split (read_line ())
let a = float_of_string (List.nth temp 0)
let b = float_of_string (List.nth temp 1)
let _ = print_endline (string_of_float (area func a b 0.001))
let _ = print_endline (string_of_float (volume func a b 0.001))
