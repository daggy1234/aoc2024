module Day01 where
import Data.List (sort)
import Data.List.Split (splitOn)

parseLine :: String -> (Int, Int)
parseLine l = 
    let [x, y] = take 2 (splitOn "   " l)
    in (read x, read y)

parser :: String -> ([Int], [Int])
parser inp = sortInps (listAccum (map parseLine (splitOn "\n" inp)))

listAccum :: [(Int, Int)] -> ([Int], [Int])
listAccum pInp = foldl (\(fAcc, sAcc) (x, y) -> (x : fAcc, y : sAcc)) ([], []) pInp

sortInps :: ([Int], [Int]) -> ([Int], [Int])
sortInps (x,y) = (sort x, sort y)

processInps :: ([Int], [Int]) -> Int
processInps (x,y) = sum [abs (a - b)| (a,b) <- zip x y]

join :: Show a =>  String -> [a] -> String
join _ [] = ""
join delimiter (x:xs) = (show x) ++ delimiter ++ (join delimiter xs)

freqCounter :: [Int] -> [(Int, Int)]
freqCounter inp = map (\x -> ([head x], length x)) (group (sort inp))

part1 :: String -> String
part1 inp = show (processInps (parser inp))

solve :: String -> String
solve inp = part1 inp

