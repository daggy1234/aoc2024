module Day02 where
import Data.List (sort)
import Data.List.Split (splitOn)

parseLine :: String -> [Int]
parseLine l =  map read (splitOn " " l)

parser :: String -> [[Int]]
parser inp =  map parseLine (splitOn "\n" inp)

recursiveCheck :: [Int] -> Bool
recursiveCheck [] = True
recursiveCheck [_] = True
recursiveCheck (x:y:xs) = (procd >=1 && procd <= 3) && recursiveCheck (y:xs) where procd = abs (x - y)

linecomp :: [Int] -> Bool
linecomp inpl = (reverse sortinpl) == inpl || sortinpl == inpl where sortinpl = sort inpl


part1 :: [[Int]] -> String
part1 inp = show (sum [1 | (a,b) <- zip (map linecomp inp) (map recursiveCheck inp), a && b])

join :: Show a =>  String -> [a] -> String
join _ [] = ""
join delimiter (x:xs) = (show x) ++ delimiter ++ (join delimiter xs)



-- part1 :: String -> String
-- part1 inp = show (processInps (parser inp))



solve :: String -> String
solve inp =  mconcat ["Part 1: ", part1s, "\n"]
    where
        part1s = part1 (parser inp)

