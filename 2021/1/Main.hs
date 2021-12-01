import System.Environment (getArgs)

getData :: String -> IO [Int]
getData fileName = do
  content <- readFile fileName
  pure $ map (\x -> read x :: Int) $ lines content

solve :: [(Int, Int)] -> Int
solve = foldl (\a (x, y) -> if x /= 0 && y > x then a+1 else a) 0

main :: IO ()
main = do
  args <- getArgs
  nums <- getData (head args)

  print $ solve (prepInput 1 nums)
  print $ solve (prepInput 3 nums)
  where
    prepInput :: Int -> [Int] -> [(Int, Int)]
    prepInput zs nums =
      let zl = replicate zs 0
      in zip (zl ++ nums) (reverse (zl ++ reverse nums))
