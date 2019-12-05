import System.IO
import Data.Map
import Data.Char
import Data.List
import qualified Data.Text    as Text
import qualified Data.Text.IO as Text
import Control.Monad

-- function to calculate the frequency of all the characters
-- strFreq x = Data.Map.toList $ Data.Map.fromListWith (+) [(c, 1) | c <- x]

main = do
    ls <- fmap Text.lines (Text.readFile "input")
    
    putStrLn (show ls)
    putStrLn (ls!!3)

 -- this is incomplete! 
 -- TODO: come back to this later!
        







        