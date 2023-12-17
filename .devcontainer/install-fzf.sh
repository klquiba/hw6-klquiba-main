# (c) 2022- Spiros Papadimitriou <spapadim@gmail.com>
#
# This file is released under the MIT License:
#    https://opensource.org/licenses/MIT
# This software is distributed on an "AS IS" basis,
# WITHOUT WARRANTY OF ANY KIND, either express or implied.

GITHUB_REPO=junegunn/fzf
VARIANT=${VARIANT:-linux_amd64}
INSTALL_ROOT=${INSTALL_ROOT:-/usr/local/bin}

PROGNAME=$(basename "$0")
function msg () {
  echo "${PROGNAME}: $@" 2>&1
}

# See, e.g., https://gist.github.com/steinwaywhw/a4cd19cda655b8249d908261a62687f8
# for example of GitHub API endpoint to get release info
URL=$(
  curl -s "https://api.github.com/repos/${GITHUB_REPO}/releases/latest" |
  jq -r '.assets[] | select(.content_type == "application/gzip") | .browser_download_url | select(.|test("'"${VARIANT}"'"))'
)

if [[ -z "$URL" ]]; then
  msg "no release tarball of '${GITHUB_REPO}' found for '$VARIANT'"
  exit 1
fi

# Fetch and untar into destination
msg "downloading and extracting"
(
  cd "${INSTALL_ROOT}" &&
  curl -L -s "$URL" | tar --keep-newer-files -zxf -
)