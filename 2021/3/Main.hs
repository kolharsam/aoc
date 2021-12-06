import System.Environment (getArgs)

getData :: String -> IO [String]
getData fileName = do
  content <- readFile fileName
  pure . lines $ content

calculateGammaRate :: [String] -> Int
calculateGammaRate = undefined

calculateEpsilonRate :: [String] -> Int
calculateEpsilonRate = undefined

solve :: [String] -> Int
solve l = calculateGammaRate l * calculateEpsilonRate l

main :: IO ()
main = do
  fileNames <- getArgs
  nums <- getData (head fileNames)

  print . solve $ nums
