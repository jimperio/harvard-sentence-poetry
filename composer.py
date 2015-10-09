from __future__ import print_function

import argparse
import random


def compose(num_strophes, num_lines, has_refrain):
  sentences = load_sentences('harvard-sentences.txt')
  refrain = None
  if has_refrain:
    refrain = random_sentence(sentences)
  strophes = []
  for _ in xrange(num_strophes or random.randint(2, 4)):
    strophes.append(
      create_strophe(sentences,
                     num_lines or random.randint(2, 4),
                     refrain)
      )
  return '\n\n'.join(strophes)

def load_sentences(path):
  sentences = []
  with open('harvard-sentences.txt', 'rb') as f:
    for line in f.readlines():
      if line.startswith('#'):
        continue
      sentences.append(line.strip())
  return sentences

def create_strophe(sentences, num_lines, refrain=None):
  lines = [random_sentence(sentences) for _ in xrange(num_lines)]
  if refrain:
    lines.pop()
    lines.append(refrain)
  return '\n'.join(lines)

def random_sentence(sentences):
  return random.choice(sentences)


if __name__ == "__main__":
  parser = argparse.ArgumentParser(description='Generate poem-like text.')
  parser.add_argument('-s', '--num-strophes', default=None, type=int,
                      help='Number of strophes (stanzas) to generate. '\
                           '(Default: 2 to 4)')
  parser.add_argument('-l', '--num-lines', default=None, type=int,
                      help='Number of lines per strophe. '\
                           '(Default: 2 to 4, varying per strophe)')
  parser.add_argument('--refrain', action='store_true', dest='has_refrain',
                      help='Use a refrain. (Default: no refrain)')
  args = parser.parse_args()
  print(compose(**vars(args)))
