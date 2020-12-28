import qualified Data.List    as L
import qualified Data.Map     as M
import qualified Data.Text    as T
import qualified Data.Text.IO as T

strFreq :: String -> [(Char, Int)]
strFreq x = M.toList $ M.fromListWith (+) [(c, 1) | c <- x]

textToStringList :: [T.Text] -> [String]
textToStringList = L.map T.unpack

nOfALetter :: Int -> String -> Bool
nOfALetter n str =
    let freqs = strFreq str
        in
            any (\(_, num) -> num == n) freqs

checkDiff :: [(Char, Char)] -> String
checkDiff zipped = [x | (x,y) <- zipped, x == y]

findDiff :: [String] -> [String]
findDiff xs = foldl (\acc (s1, s2) ->
    if length (checkDiff (zip s1 s2)) == (length s1 - 1)
        then s1:acc
        else acc
    ) [] ([(x,y) | x <- xs, y <- xs, x /= y])

resString :: [String] -> String
resString xs = [c1 | (c1, c2) <- zip (head xs) (xs !! 1), c1 == c2] 

diffWithOne :: [String] -> String
diffWithOne strList = 
    let diffList = findDiff strList
        in
            resString diffList

main :: IO ()
main = do
    ls <- fmap T.lines (T.readFile "input")
    let strList = textToStringList ls

    -- part 1
    let num2 = length (filter (nOfALetter 2) strList)
    let num3 = length (filter (nOfALetter 3) strList)
    print $ num2 * num3
    -- part 2
    print $ diffWithOne strList
