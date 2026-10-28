# Part A: Feed-Forward Neural Networks

A feed-forward neural network passes information from input to output through successive
layers without recurrent connections. Here, its inputs are bag-of-words features: token
frequencies representing each news article. This implementation adapts Surdeanu and
Valenzuela-Escárcega (2023) and uses AG News,
which contains 120,000 training articles and 7,600 test articles in four categories: World,
Sports, Business, and Sci/Tech (Zhang et al., 2015).

Pandas loads each article's class index, title, and description. The local CSV files have
headers. The title and description are joined and lowercased. Pandas replaces backslashes
with spaces; additional cleaning decodes HTML character references, removes tags and URLs,
and replaces corrupted `#NAME?` fields with empty strings. NLTK's `word_tokenize()` splits
the combined text into tokens, stored in a new dataframe column (Bird et al., 2009).

An 80/20 split reserves 24,000 training-file articles for development and leaves 96,000 for
fitting the model. The vocabulary is learned exclusively from this fitting split. Tokens
occurring more than ten times receive individual integer identifiers; all other tokens map
to `[UNK]`. Each document becomes a 17,369-dimensional vector with one position per vocabulary
entry. Each value counts that token's occurrences; absent tokens have value zero. This
representation retains frequency but discards word order and provides no explicit
representation of synonymy.
Sparse dictionaries store the counts, and a PyTorch `Dataset` creates dense float32 vectors
as batches are requested.

The network applies input dropout, a linear layer with 50 hidden units, ReLU, hidden dropout,
and a linear layer producing four logits, or unnormalized class scores. The hidden layer
learns weighted combinations of token counts. ReLU introduces nonlinearity; dropout randomly
zeros inputs and hidden activations with probability 0.3 during training to reduce overfitting
(Goodfellow et al., 2016; Srivastava et al., 2014).

Training uses shuffled batches of 500 for five epochs. `CrossEntropyLoss` takes the logits
and zero-based integer labels, combining log-softmax with negative log-likelihood. An
additional softmax layer is unnecessary. Adam updates the parameters using learning rate
0.001 and weight decay 0.00001 (Kingma & Ba, 2015). Each step clears gradients, computes
predictions and loss, backpropagates, and updates the weights.

Development loss and accuracy monitor learning without updating parameters. After training,
the test set receives identical cleaning, tokenization, and encoding with the fixed training
vocabulary. `model.eval()` disables dropout, and `torch.no_grad()` disables gradient tracking.
The largest logit determines the predicted class. Accuracy, per-class precision, recall, F1,
and a confusion matrix quantify performance and show which topics are confused.
