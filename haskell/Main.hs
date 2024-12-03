module Main where

import Day01 (solve)
import System.Environment (getArgs)
import Text.Printf (printf)
import Data.String (String)

main :: IO ()
main = do
  args <- getArgs
  case args of
    [n] -> runDay (read n)
    _ -> print "Please enter a day from 1 to 25"

runDay :: Int -> IO ()
runDay n = do
  input <- getRawInput n False
  let solution = solutions !! (n - 1)
  putStrLn (solution input)

getRawInput :: Int -> Bool -> IO String
getRawInput d test = readFile ((printf "data/day%02d/" d) ++ (if test then "test" else "inp") ++ ".txt")

solutions :: [String -> String]
solutions =
    [
        Day01.solve
    ]