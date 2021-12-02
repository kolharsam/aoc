import System.Environment (getArgs)

getData :: String -> IO [(String, Int)]
getData fileName = do
  content <- readFile fileName
  pure $ map (\x -> read x :: Int) $ lines content

solve :: [Bool] -> Int
solve = length . filter (== True)

data Position = Position {
    _unX :: Int
  , _unZ :: Int
  , _unAim :: Int
}

main :: IO ()
main = do
  args <- getArgs
  nums <- getData (head args)

  print $ solve (prepInput 1 nums)
  print $ solve (prepInput 3 nums)
  where
    prepInput :: Int -> [Int] -> [Bool]
    prepInput zs nums = zipWith (<) nums (drop zs nums)
