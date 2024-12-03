module Main where

import Day01 (solve)
import Day02 (solve)
import Day03 (solve)

import System.Environment (getArgs)
import Text.Printf (printf)
import Options.Applicative

data Options = Options
  { day  :: Int
  , test :: Bool
  }


optionsParser :: Parser Options
optionsParser = Options
  <$> argument auto
      ( metavar "DAY"
     <> help "Day number to run (1-25)" )
  <*> switch
      ( long "test"
     <> short 't'
     <> help "Run in test mode" )

main :: IO ()
main = do
  options <- execParser opts
  let dayNumber = day options
      isTest = test options
  runDay dayNumber isTest
  where
    opts = info (optionsParser <**> helper)
      ( fullDesc
     <> progDesc "Run the Advent of Code solutions for a given DAY"
     <> header "Advent of Code Runner" )

runDay :: Int -> Bool -> IO ()
runDay n isTest = do
  input <- getRawInput n isTest
  let solution = solutions !! (n - 1)
  putStrLn (solution input)

getRawInput :: Int -> Bool -> IO String
getRawInput d test = readFile ((printf "data/day%02d/" d) ++ (if test then "test" else "inp") ++ ".txt")

solutions :: [String -> String]
solutions =
    [
        Day01.solve,
        Day02.solve,
        Day03.solve
    ]