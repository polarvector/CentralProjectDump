from chessdictvalidator import isValidChessBoard

validBoard = {
    '1h': 'bk', '2a': 'wq', '2g': 'br', '5h': 'bp', '3e': 'wr', '4d': 'wn', '6c': 'wb',
    '7f': 'bn', '8a': 'bp', '3c': 'wp', '1b': 'wk', '6g': 'bb', '4h': 'wr', '8e': 'bp'
}
positionOutOfBounds = {
    '9a': 'bk', '2a': 'wq', '2g': 'br', '5h': 'bp', '3e': 'wr'
}
invalidColor = {
    '1h': 'yk', '2a': 'wq', '2g': 'br', '5h': 'bp', '3e': 'wr'
}
invalidPiece = {
    '1h': 'bk', '2a': 'wq', '2g': 'br', '5h': 'bz', '3e': 'wr'
}
tooManyPieces = {
    '1h': 'bk', '2a': 'wq', '2g': 'br', '5h': 'bp', '3e': 'wr', '4d': 'wn', '6c': 'wb',
    '7f': 'bn', '8a': 'bp', '3c': 'wp', '1b': 'wk', '6g': 'bb', '4h': 'wr', '8e': 'bp',
    '5a': 'bp', '6a': 'bp', '7a': 'bp', '8b': 'bp'
}
mixedBoard = {
    '1h': 'bk', '2a': 'wq', '2g': 'br', '5h': 'bp', '3e': 'wr', '9a': 'bk', '3b': 'yk', 
    '4f': 'bz', '7d': 'wr', '2h': 'bk', '5g': 'bp'
}

isValidChessBoard(validBoard)
isValidChessBoard(positionOutOfBounds)
isValidChessBoard(invalidColor)
isValidChessBoard(invalidPiece)
isValidChessBoard(tooManyPieces)

