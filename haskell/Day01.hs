module Day01 where
import Data.List (sort, group)
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
freqCounter inp = map (\x -> (head x, length x)) (group (sort inp))

part1 :: String -> String
part1 inp = show (processInps (parser inp))

ctr :: [Int] -> [(Int, Int)] -> Int -> Int
ctr [] _ summ = summ
ctr (x:xs) freqs summ =
    case filter (\(a, _) -> a == x) freqs of
        [] -> ctr xs freqs summ
        ((_, b):_) -> ctr xs freqs (summ + (b*x))

part2 :: String -> String
part2 inp = show (ctr a (freqCounter b) 0)  where (a,b) = parser inp

solve :: String -> String
solve inp =  mconcat ["Part 1: ", part1s, "\n", "Part 2: ", part2s]
    where
        part1s = part1 inp
        part2s = part2 inp

