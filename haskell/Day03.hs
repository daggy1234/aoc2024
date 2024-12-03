module Day03 where

import Text.Regex.TDFA
import Data.List (isPrefixOf)

findALl :: String -> String -> [String]
findALl inp reg = getAllTextMatches (inp =~ reg) :: [String]

mulProc :: String -> Int
mulProc i = foldl (\acc x -> acc * (read x)) 1 (findALl i "[0-9]+")

processor :: [String] -> Bool -> Int
processor [] _ = 0
processor (x:xs) activated
    | isPrefixOf "don't" x = processor xs False 
    | isPrefixOf "do(" x = processor xs True
    | otherwise = (if activated then (mulProc x) else 0)  + processor xs activated

solve :: String -> String
solve inp = mconcat ["Part 1: ", p1s, "\n", "Part 2: ", p2s]
    where
        p1s = show $ sum $ map mulProc $ findALl inp  "mul\\([0-9]+,[0-9]+\\)"
        p2s = show $ processor (findALl inp  "mul\\([0-9]+,[0-9]+\\)|do\\(\\)|don't\\(\\)") True
