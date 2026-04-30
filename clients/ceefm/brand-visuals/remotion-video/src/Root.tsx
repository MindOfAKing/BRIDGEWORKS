import React from 'react';
import {Composition} from 'remotion';
import {CEEFMVideo, Lang, Variant} from './Video';

const variants: Array<{variant: Variant; width: number; height: number}> = [
  {variant: '16x9', width: 1920, height: 1080},
  {variant: '1x1', width: 1080, height: 1080},
  {variant: '9x16', width: 1080, height: 1920},
];

const langs: Lang[] = ['EN', 'HU'];
const durations = [15, 30] as const;

export const Root: React.FC = () => {
  return (
    <>
      {durations.flatMap((duration) =>
        langs.flatMap((lang) =>
          variants.map(({variant, width, height}) => (
            <Composition
              key={`${duration}-${variant}-${lang}`}
              id={`ceefm-ad-${duration}s-${variant}-${lang}`}
              component={CEEFMVideo}
              durationInFrames={duration * 30}
              fps={30}
              width={width}
              height={height}
              defaultProps={{duration, lang, variant}}
            />
          ))
        )
      )}
    </>
  );
};
