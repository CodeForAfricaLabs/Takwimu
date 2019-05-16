/* eslint-disable react/no-danger */
import React, { useState, useEffect } from 'react';
import { PropTypes } from 'prop-types';

import { withStyles, Typography } from '@material-ui/core';

import classNames from 'classnames';

import leftArrow from '../../../assets/images/left-arrow.svg';
import rightArrow from '../../../assets/images/right-arrow.svg';
import useScrollListener from '../../../useScrollListener';

const styles = theme => ({
  root: {
    width: '100%'
  },
  carouselWrapper: {
    width: '100%',
    height: '16.813rem'
  },
  carousel: {
    zIndex: 1,
    width: '100%',
    height: '16.813rem',
    borderRadius: '0.25rem',
    backgroundColor: '#f6f6f6',
    display: 'flex',
    [theme.breakpoints.up('md')]: {
      width: '44.265625rem' // .75 of lg
    },
    [theme.breakpoints.up('lg')]: {
      width: '58.4375rem'
    }
  },
  carouselFixed: {
    position: 'fixed',
    top: '6.25rem',
    borderTopLeftRadius: 0,
    borderTopRightRadius: 0,
    zIndex: 1,
    '&:after': {
      // shadow
      content: '""',
      width: '100%',
      height: '100%',
      position: 'absolute',
      boxShadow: '0 2px 6px 4px rgba(0, 0, 0, 0.2)',
      clipPath: 'inset(0 0 -0.75rem 0)' // bottom only shadow
    }
  },
  arrow: {
    width: '6%', // 53px / 934px,
    height: '100%',
    display: 'flex',
    aligItems: 'center',
    justifyContent: 'center',
    backgroundColor: '#f6f6f6',
    cursor: 'pointer',
    position: 'relative',
    zIndex: 1,
    '&:before': {
      // shadow
      content: '""',
      position: 'absolute',
      height: '100%',
      width: '100%',
      zIndex: 1,
      backgroundColor: '#f6f6f6'
    },
    '&:after': {
      // shadow
      content: '""',
      position: 'absolute',
      top: '5%',
      height: '90%',
      width: '50%',
      zIndex: 0,
      boxShadow: '0 2px 6px 4px rgba(0, 0, 0, 0.2)'
    },
    '&:first-child': {
      '&:before': {
        backgroundImage: `url(${leftArrow})`,
        backgroundRepeat: 'no-repeat',
        backgroundPosition: 'center'
      },
      '&:after': {
        left: '50%'
      }
    },
    '&:last-child': {
      '&:before': {
        backgroundImage: `url(${rightArrow})`,
        backgroundRepeat: 'no-repeat',
        backgroundPosition: 'center'
      },
      '&:after': {
        right: '50%'
      }
    }
  },
  content: {
    overflow: 'scroll',
    width: '88%',
    height: '100%',
    display: 'flex'
  },
  profile: {
    cursor: 'pointer',
    margin: '2.5rem 1.875rem',
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
    textAlign: 'center'
  },
  profilePicture: {
    width: '7.125rem',
    height: '7.125rem',
    borderRadius: '50%'
  },
  profilePictureSelected: {
    border: `solid 6px ${theme.palette.primary.main}`
  },
  profileTitle: {
    fontFamily: theme.typography.fontText,
    fontSize: '0.875rem',
    fontWeight: '600',
    fontStyle: 'normal',
    fontStretch: 'normal',
    lineHeight: 'normal',
    letterSpacing: 'normal',
    width: '152px'
  },
  profileName: {
    fontFamily: theme.typography.fontText,
    color: theme.palette.primary.main,
    textDecoration: 'underline',
    fontSize: '0.875rem',
    fontStyle: 'normal',
    fontStretch: 'normal',
    lineHeight: 'normal',
    letterSpacing: 'normal',
    width: '152px'
  },
  profileNameSelected: {
    color: 'black',
    textDecoration: 'none'
  }
});

function Topic({ classes, data }) {
  const widgets = data
    .filter(x => x.type === 'indicator' && x.value.widget.type === 'entities')
    .map(x => x.value.widget);
  const isOverThreshold = useScrollListener(100, '<', 'political-figures');
  const [selectedIndex, setSelectedIndex] = useState(widgets.length / 2);

  useEffect(() => {
    const profile = document.getElementById(`profile-${selectedIndex}`);
    profile.scrollIntoView({ inline: 'nearest', block: 'nearest' });
  }, [selectedIndex]);

  return (
    <div id="political-figures" className={classes.root}>
      <div className={classes.carouselWrapper}>
        <div
          className={classNames(classes.carousel, {
            [classes.carouselFixed]: isOverThreshold
          })}
        >
          <div
            role="button"
            tabIndex={0}
            className={classes.arrow}
            onClick={() =>
              selectedIndex > 0 && setSelectedIndex(selectedIndex - 1)
            }
            onKeyUp={() => null}
          />
          <div className={classes.divider} />

          <div id="carousel-content" className={classes.content}>
            {widgets.map((widget, index) => (
              <div
                role="button"
                tabIndex={0}
                id={`profile-${index}`}
                className={classes.profile}
                onClick={() => setSelectedIndex(index)}
                onKeyUp={() => null}
              >
                <img
                  alt=""
                  className={classNames(classes.profilePicture, {
                    [classes.profilePictureSelected]: selectedIndex === index
                  })}
                />
                <Typography
                  className={classNames(classes.profileName, {
                    [classes.profileNameSelected]: selectedIndex === index
                  })}
                >
                  {widget.value.entities[0].name}
                </Typography>
                <Typography className={classes.profileTitle}>
                  {widget.value.title}
                </Typography>
              </div>
            ))}
          </div>

          <div className={classes.divider} />
          <div
            role="button"
            tabIndex={0}
            className={classes.arrow}
            onClick={() =>
              selectedIndex < widgets.length - 1 &&
              setSelectedIndex(selectedIndex + 1)
            }
            onKeyUp={() => null}
          />
        </div>
      </div>
      <Typography
        className={classes.body}
        dangerouslySetInnerHTML={{
          __html: widgets[selectedIndex].value.entities[0].description
        }}
      />
    </div>
  );
}

Topic.propTypes = {
  classes: PropTypes.shape({}).isRequired,
  data: PropTypes.shape({}).isRequired
};

export default withStyles(styles)(Topic);
