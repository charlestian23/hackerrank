let rec sum_of_odds sum =
  try
    let input = read_line() in
    match input with 
      | "" -> sum
      | x -> let num = int_of_string x in if num mod 2 = 1 || num mod 2 = -1 then sum_of_odds(sum + num) else sum_of_odds sum
  with End_of_file -> sum

let _ = print_int (sum_of_odds 0)