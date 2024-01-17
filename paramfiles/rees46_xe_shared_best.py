from collections import OrderedDict
gru4rec_params = OrderedDict([
('loss', 'cross-entropy'),
('constrained_embedding', True),
('embedding', 0),
('elu_param', 0),
('layers', [512]),
('n_epochs', 10),
('batch_size', 240),
('dropout_p_embed', 0.45),
('dropout_p_hidden', 0.0),
('learning_rate', 0.065),
('momentum', 0.0),
('n_sample', 2048),
('sample_alpha', 0.5),
('bpreg', 0.0),
('logq', 1.0)
])
