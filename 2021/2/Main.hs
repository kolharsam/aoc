{-# LANGUAGE RecordWildCards #-}

import System.Environment (getArgs)
-- NOTE: would've been easier with Lenses

type Instruction = (String, Int)

getData :: String -> IO [Instruction]
getData fileName = do
  content <- readFile fileName
  pure $ map (readLine . words) $ lines content
  where
    readLine :: [String] -> Instruction
    readLine [inst, numStr] = (inst, read numStr)
    readLine _ = error "WTF?"

solve :: Position -> AimChoice -> [Instruction] -> Position
solve startPos ac =
  flip foldl startPos $ \pos (inst, num) -> case inst of
    "forward" -> moveForward num ac pos
    "up"      -> updateAimOrDepth num ac pos
    "down"    -> updateAimOrDepth (-num) ac pos
    _ -> undefined

makeScore :: Position -> Int
makeScore ps@Position{..} = _unX * _unZ

data Position = Position {
    _unX   :: Int
  , _unZ   :: Int
  , _unAim :: Int
} deriving (Show, Eq)

type PositionUpdater = Int -> AimChoice -> Position -> Position

moveForward :: PositionUpdater
moveForward num ac pos@Position{..} =
  if ac == WithoutAim
    then pos { _unX = _unX + num }
    else pos { _unX = _unX + num, _unZ = _unZ + (_unAim * num) }

updateAimOrDepth :: PositionUpdater
updateAimOrDepth num ac pos@Position{..} =
  if ac == WithoutAim
    then pos { _unZ = _unZ + num }
    else pos { _unAim = _unAim + num }

data AimChoice = WithAim | WithoutAim
  deriving(Eq)

main :: IO ()
main = do
  args <- getArgs
  input <- getData $ head args
  
  showScore $ solve' WithoutAim input
  showScore $ solve' WithAim input
  where
    start = Position 0 0 0
    solve' = solve start
    showScore = print . abs . makeScore
