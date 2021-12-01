import System.Environment (getArgs)

getData :: String -> IO [Int]
getData fileName = do
  content <- readFile fileName
  pure $ map (\x -> read x :: Int) $ lines content

solve :: [Bool] -> Int
solve = length . filter (== True)

main :: IO ()
main = do
  args <- getArgs
  nums <- getData (head args)

  print $ solve (prepInput 1 nums)
  print $ solve (prepInput 3 nums)
  where
    prepInput :: Int -> [Int] -> [Bool]
    prepInput zs nums = zipWith (<) nums (drop zs nums)
