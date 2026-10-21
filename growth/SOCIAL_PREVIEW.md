# GitHub social preview

## Asset

`assets/social-preview.png` is a 1280 × 640 PNG (56 KB) designed for repository
links shared on LinkedIn and other social platforms. It presents the verified
learning-path size and the synthetic-payment teaching hook. The artwork uses
the same colors and typography as `assets/cover.svg`.

## Current state

Checked 2026-10-22: the public repository page exposes GitHub's generated
`opengraph.githubassets.com` image. No custom social preview image is configured.
Adding the PNG to the repository does not set that repository-level option.

## Set the image

After this PR is merged, open the repository's **Settings → Social preview →
Edit**, upload `assets/social-preview.png`, and save. GitHub recommends 1280 ×
640 pixels for best display and requires a PNG, JPG, or GIF under 1 MB.

Then open the public repository page and confirm its `og:image` points to the
custom preview. This updates the share presentation; it does not guarantee more
clicks or stars. See [GitHub's instructions](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/customizing-your-repositorys-social-media-preview).

